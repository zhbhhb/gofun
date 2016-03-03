package main

import (
        "fmt"
        "math/rand"
       )

func rand_generator_2() chan int {
    out := make(chan int)
    go func() {
        for {
            out <- rand.Int()
        }
    }()
    return out
}

func main() {
    rand_service_handler := rand_generator_2()
    for i:=0; i< 10; i++ {
        fmt.Printf("%d\n", <-rand_service_handler)
    }
}
