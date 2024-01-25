# Install flask from pip3 by using puppet
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}