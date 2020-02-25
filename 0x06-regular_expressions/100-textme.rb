#!/usr/bin/env ruby
puts ARGV[0].scan(/((?<=from:)\W?[a-zA-Z 0-9]+|(?<=flags:).+?(?=\])|(?<=to:)\W?\d+)/).join(",")
