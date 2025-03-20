<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      form {
        border: 1px solid #999;
        border-radius: 4px;
        padding: 12px 8px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
        max-width: 500px;
        margin: 128px auto 0;
      }

      label {
        display: flex;
        flex-direction: column;
        gap: 4px;
        width: 100%;
      }

      label input {
        padding: 4px;
        font-size: 16px;
        border: 1px solid #cdcdcd;
        border-radius: 4px;
      }

      label input:focus {
        outline: none;
        border-color: #a0a0a0;
      }

      .radio {
        display: flex;
        flex-direction: column;
        gap: 4px;
        width: 100%;
      }

      .radio div {
        display: flex;
        gap: 8px;
      }

      .radio label {
        display: flex;
        flex-direction: row;
        gap: 4px;
        align-items: center;
      }

      .radio input {
        margin-right: 4px;
      }

      button {
        padding: 8px 16px;
        font-size: 16px;
        background-color: #710000;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
      }
    </style>
  </head>
  <body>
    <form action="process.php" method="post">
      <label for="mac-address">Client device MAC address: <input type="text" name="mac-address" id="mac-address" /></label>
      <div class="radio">
        Version:
        <div><label for="v4">DHCPv4 <input type="radio" name="dhcp" id="v4" value="4" /></label>
        <label for="v6">DHCPv6 <input type="radio" name="dhcp" id="v6" value="6" /></label></div>
      </div>
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
