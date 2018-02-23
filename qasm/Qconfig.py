APItoken = 'ea651b9c3625470aa6969e5e6b7ca7bf585a3714f1eb2da917f896b3e80e11a03ee6d66704c869cab8a5c41a6d3a9c54da94295b178d180d10ae111b213fff03'
config = {'url': 'https://quantumexperience.ng.bluemix.net/api'}

if 'APItoken' not in locals():
    raise Exception('Please set up your access token. See Qconfig.py.')
