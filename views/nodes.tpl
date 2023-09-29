<html>
    <title>
        Node Availability Report
    </title>
    <body>
        <table>
            %for key in template_data:
            <tr>
                <td>
                    {{key}}
                </td>
                <td>
                    {{template_data[key]}}
                </td>
            </tr>
            %end
        </table>
    </body>
</html>
