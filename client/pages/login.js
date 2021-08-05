export default function login() {
  return (
    <>
      <Head>
        <title>FACES-21</title>
      </Head>
     
     <Flex height="100vh"background="green.100"alignItems="center" justifyContent="center" >
         <Flex direction="column" background="green.200" p={12} rounded={6}>
           <Heading mb={6}>Log In</Heading>
           <Input placeholder="Roll No" variant="filled"mb={10} type="number"/>
           <Input placeholder="*******" variant="filled"mb={10} type="password"/>
           <Button colorScheme="green">Log IN</Button>
           
         </Flex>
      </Flex> 

    </>
  );
}
