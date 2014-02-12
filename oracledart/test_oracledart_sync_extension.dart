// Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

library test_oracledart_sync_extension;

import 'oracledart_synchronous_extension.dart';

void check(bool condition, String message) {
  if (!condition) {
    throw new StateError(message);
  }
}

void main() {
  for (var i = 0; i < 10; i++) {
    OracleConnection connection = new OracleConnection();
    connect(connection, "system", "oracle", "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=orcl)(SERVER=DEDICATED)))");

    OracleResultset resultset = new OracleResultset();    
    select(connection, resultset, "select employee_id, last_name from hr.employees");

    while (resultset.next()) {
        print("${resultset.getInt(1)} ${resultset.getString(2)}");
    }
  }
}
