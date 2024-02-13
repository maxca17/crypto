package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	listen, err := net.Listen("tcp", "127.0.0.1:8080")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer listen.Close()
	fmt.Println("Server listening on 127.0.0.1:8080")

	for {
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println(err)
			continue
		}
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()
	reader := bufio.NewReader(conn)
	for {
		message, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Print("Received: ", string(message))
		conn.Write([]byte(message))
	}
}
