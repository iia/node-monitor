<html>
    <head>
        <meta http-equiv="refresh" content="30">
        <title>
            Node Availability Report
        </title>
    </head>
    <body>
        <table>
            %for key in template_data:
            <tr>
                <td>
                    <font color="green"><strong>{{key}}</strong></font>
                </td>
                <td>
                    <font color="orange">{{template_data[key]}}</font>
                </td>
            </tr>
            %end
        </table>
    </body>
</html>
