#Fixes typo in wordpress settings
exec { 'fix-wordpress':
    command    => '/bin/sed -i s"/phpp/php/" /var/www/html/wp-settings.php',
}
