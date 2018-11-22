from scrapy.utils.markup import remove_tags
import re

text = '''
<?xml version="1.0" encoding="utf-16"?>

<consultaPasivosClienteRequest1 xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <RequestHeader>

    <Authentication>

     

      

    </Authentication>

    <Region>

      <SourceBank>GT01</SourceBank>

      <DestinationBank>GT01</DestinationBank>

    </Region>

  </RequestHeader>

  <consultaPasivosClienteRequest>

    <CUSTOMER_ID>6000298</CUSTOMER_ID>

    <LIABILITY_TYPE>ALL</LIABILITY_TYPE>

  </consultaPasivosClienteRequest>

</consultaPasivosClienteRequest1>

RESPONSE:

<?xml version="1.0" encoding="utf-16"?>

<consultaPasivosClienteResponse xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <ResponseHeader>

    <messageId>34</messageId>

    <successIndicator>AUTHERROR</successIndicator>

    <messages>(MsjId:1283699) Fallo en la autenticación del usuario</messages>

  </ResponseHeader>

  <consultaPasivosClienteResponse1 />

</consultaPasivosClienteResponse>
'''

print(re.sub(r'\s{2,}', '\n', remove_tags(text)))
