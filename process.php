<?php

  $mac_address = $_POST['mac-address'];
  $dhcp = $_POST['dhcp'];

  $command = escapeshellcmd("python3 network_config.py $mac_address $dhcp");
  $output = shell_exec($command);

  echo $output;
  
?>