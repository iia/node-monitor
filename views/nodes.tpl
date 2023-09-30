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
                <td color="orange">
                    <strong>{{key}}</strong>
                </td>
                <td color="purple">
                    {{template_data[key]}}
                </td>
            </tr>
            %end
        </table>
    </body>
</html>
