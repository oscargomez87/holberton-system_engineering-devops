# Configures clean ubuntu 16.04 with nginx

exec { 'apt-get-update':
  command     => '/usr/bin/apt-get update',
}

package { 'Install nginx':
  name     => 'nginx',
  provider => apt,
  ensure   => installed,
  require  => Exec['apt-get-update'],
}


file_line { 'Add header':
  ensure  => present,
  path    => '/etc/nginx/sites-enabled/default',
  after   => '^\s*location \/ {',
  line    => "\t\tadd_header X-Served-By \$hostname;",
  require => Exec['Install nginx'],
}

service { 'nginx':
  ensure   => true,
  require  => File_line['Add header'],
}
