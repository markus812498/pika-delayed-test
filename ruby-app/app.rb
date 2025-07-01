require "bundler/inline"

# This installs and requires these gems
gemfile do
  source "https://rubygems.org"
  gem "bunny"
end

STDOUT.sync = true

BROKER_URL = ENV["BROKER_URL"]

conn = Bunny.new(BROKER_URL)
conn.start

ch = conn.create_channel

x = ch.exchange("test-delayed", :type => "x-delayed-message", :arguments => { "x-delayed-type" =>  "direct" })
q = ch.queue("test-delayed").bind(x, :routing_key => "test-delayed")

x.publish("hello!", :routing_key => q.name, :headers => { "x-delay" => 1000 })
puts "published to #{q.name}"
conn.close
