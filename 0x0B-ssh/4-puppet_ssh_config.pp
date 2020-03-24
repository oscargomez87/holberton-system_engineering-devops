# Configures ssh client to use specific pvkey and not use password

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  match  => '^PasswordAuthentication',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
