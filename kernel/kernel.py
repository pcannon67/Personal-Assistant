#!/usr/bin/python3

import attwordListener
import speechToText

class Kernel:
  """
  Class maintaining run of the whole application.
  """


  def __init__(self):
    """
    Initialization of the kernel.

    Returns:
      None
    """

    # global config
    self.minPort = 5000
    self.maxPort = 5999
    self.maxRetries = 99

    # attention word module config
    self.attwordConfig = {'path': '../modules/dummy/dummy.py', 'attentionWord': 'Fenix', 'threshold': 1}
    self.attwordConfig['minPort'] = self.minPort
    self.attwordConfig['maxPort'] = self.maxPort
    self.attwordConfig['maxRetries'] = self.maxRetries

    # speech-to-text module config
    self.speechToTextConfig = {'path': '../modules/dummy/dummy.py', 'dbToken': 'someToken'}
    self.speechToTextConfig['minPort'] = self.minPort
    self.speechToTextConfig['maxPort'] = self.maxPort
    self.speechToTextConfig['maxRetries'] = self.maxRetries

    # init wrappers
    self.attwordListener = attwordListener.attwordListener(self.attwordConfig)
    self.speechToText = speechToText.speechToText(self.speechToTextConfig)


  def run(self):
    """
    Runs the application.

    Returns:
      None
    """

    try:
      # run all processes
      self.attwordListener.start()
      self.speechToText.start()

      # do the work
      for i in range(0, 10):
        print(self.attwordListener.sendReply({'iteration': i}))
        print(self.speechToText.sendReply({'iteration': i}))

    finally:
      # clean after all
      self.stop()


  def stop(self):
    """
    Stops all processes that have been run.

    Returns:
      None
    """

    self.attwordListener.stop()
    self.speechToText.stop()



class ConfigError(Exception):
  """
  Exception class handling module configuration error.
  """

  def __init__(self, module):
    """
    Init of the exception.

    Args:
      module (str): name of module failed to config

    Returns:
      None
    """

    self.module = module
  
  def __str__(self):
    """
    Converts exception to a string.

    Returns:
      str: string representation of the exception
    """

    return 'Module "' + self.module  + '" failed to config.'



class CommunicationError(Exception):
  """
  Exception class handling communication error with the module.
  """

  def __init__(self, module, message):
    """
    Init of the exception.

    Args:
      module (str): name of module failed to communicate to
      message (str): description of the problem

    Returns:
      None
    """

    self.module = module
    self.message = message
  
  def __str__(self):
    """
    Converts exception to a string.

    Returns:
      str: string representation of the exception
    """

    return 'Communication failed with the module "' + self.module  + '" (' + self.message + ').'



# DEMO
if __name__ == '__main__':
  kernel = Kernel()
  kernel.run()
