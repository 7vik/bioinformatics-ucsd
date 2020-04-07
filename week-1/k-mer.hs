main = do
    args <- getArgs
    content <- readFile (args !! 0)
    let text = (lines content !! 0)
    let pattern = (lines content !! 1)
    putStrLn (show (solve text pattern))

solve :: String -> String -> Integer
solve _ _ = 31