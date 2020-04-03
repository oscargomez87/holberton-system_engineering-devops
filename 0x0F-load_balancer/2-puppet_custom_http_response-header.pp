# Configures ssh client to use specific pvkey and not use password

file_line { 'Add header':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => '^\s*location \/ {',
  line   => "\t\tadd_header X-Served-By \$hostname;",
}
