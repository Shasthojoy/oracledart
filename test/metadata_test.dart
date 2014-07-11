import 'package:unittest/unittest.dart';
import 'package:unittest/vm_config.dart';

import 'package:oracledart/oracledart.dart';

void main() {
  useVMConfiguration();
  OracleConnection connection = new OracleConnection.connect(
    "scott",
    "tiger",
    "(DESCRIPTION="
      "(ADDRESS=(PROTOCOL=TCP)(HOST=w8-32-12core)(PORT=1521))"
      "(CONNECT_DATA=(SERVICE_NAME=XE)(SERVER=DEDICATED)))");

  test('Test getMetadataVector', () {
    OracleResultset resultset =
        connection.select("select empno, ename from emp");
    OracleMetadataVector metadata =
        resultset.getMetadataVector();
    expect(metadata.getSize(), equals(2));
    expect(metadata.getColumnName(0), equals("EMPNO"));
    expect(metadata.getColumnName(1), equals("ENAME"));
  });

  test('Test getMetadataVector with star', () {
    OracleResultset resultset =
        connection.select("select * from emp");
    OracleMetadataVector metadata =
        resultset.getMetadataVector();
    expect(metadata.getSize(), equals(8));
    expect(metadata.getColumnName(0), equals("EMPNO"));
    expect(metadata.getColumnName(1), equals("ENAME"));
    expect(metadata.getColumnName(2), equals("JOB"));
    expect(metadata.getColumnName(3), equals("MGR"));
    expect(metadata.getColumnName(4), equals("HIREDATE"));
    expect(metadata.getColumnName(5), equals("SAL"));
    expect(metadata.getColumnName(6), equals("COMM"));
    expect(metadata.getColumnName(7), equals("DEPTNO"));
  });
}
