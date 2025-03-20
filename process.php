<?php

  $mac_address = $_POST['mac-address'];
  $dhcp = $_POST['dhcp'];

  $command = escapeshellcmd("python3 network_config.py $mac_address $dhcp");
  $output = shell_exec($command);

  $host_ip = $_SERVER['SERVER_ADDR'];

  echo "<h1 style='text-align: center; margin: 32px 0;'>Network Configuration</h1>";
  echo "Current IP address: $host_ip<br>";

  echo $output;
  
?>