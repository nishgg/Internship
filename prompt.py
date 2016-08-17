import copy

class prompt_funcs:

  response_values = {}

  # prompt a user given a dictionary of data and messages
  def prompt_user(self, prompt_dictionary):
    # for each datum, prompt the user to input the value
    for key in prompt_dictionary:
      # print the prompt
      print prompt_dictionary[key]
      # get the value from user
      answer = raw_input()
      # mutate the dictionary to store the answer
      prompt_dictionary[key] = answer
    # return the dictionary with the user input as values instead of the messages
    return prompt_dictionary

  def prompt_user_temp(self, prompt_dictionary, main_dictionary):
      # for each datum, prompt the user to input the value
      for key in prompt_dictionary:
      # print the prompt
          print prompt_dictionary[key]
          # get the value from user
          answer = raw_input()
          # mutate the dictionary to store the answer
          main_dictionary[key] = answer
      # return the dictionary with the user input as values instead of the messages
      return main_dictionary

  # format a single test case with the user prompts
  def format_test_case(self, test_case):
    # get the prompt dictionary
    prompts = test_case[0]['prompt']
    # prompt the user using the dictionary
    prompts = prompt_user(prompts)

    # insert the user inputs into the test case
    for line in test_case[1:]:
      for key in prompts:
        if key in line:
          line[key] = prompts[key]

    return test

  # format an entire test with user prompts
  def format_test(self, test):

    # for each test case, format it
    for test_case in test:
      format_test_case(test_case)
    return test

  # get an ip range
  def get_ip_range(self, ipRange):
    splitipRange = ipRange.split('-')
    lowIP = splitipRange[0]
    highIP = splitipRange[1]
    final = [lowIP]
    lowSplit = lowIP.split('.')
    highSplit = highIP.split('.')
    dif = int(highSplit[3]) - int(lowSplit[3])

    for x in range(1, dif + 1):
      newIP = copy.deepcopy(lowSplit)
      newIP[3] = str(int(newIP[3]) + x)
      final.append('.'.join(newIP))

    return final
