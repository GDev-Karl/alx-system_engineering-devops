# Install flask from pip3 by using puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}