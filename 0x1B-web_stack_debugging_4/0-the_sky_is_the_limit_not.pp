# Removes nofile limit imposed by nginx default config
exec { 'fix--for--nginx':
  command => '/usr/bin/sed -i s\'/ULIMIT="-n 15"/#ULIMIT="-n 15"/\' /etc/default/nginx && service nginx restart',
}
