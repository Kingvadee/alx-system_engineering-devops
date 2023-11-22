<<<<<<< HEAD
#!/usr/bin/env bash
=======
>>>>>>> origin/master
# Seting up my client config file
include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
<<<<<<< HEAD
  line   => '     IdentityFile $HOME/.ssh/school',
=======
  line   => '     IdentityFile ~/.ssh/school',
>>>>>>> origin/master
  replace => true,
}
