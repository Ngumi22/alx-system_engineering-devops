# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

include stdlib

file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[\s#]*IdentityFile.*$',
}

file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[\s#]*PasswordAuthentication.*$',
}
