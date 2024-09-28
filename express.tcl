

set rules {"/foo,starts_with,giant_pool" 
    "/fi,starts_with,giant_pool"
    "/fum,starts_with,giant_pool"
    "/abc,starts_with,alphabet_pool"
    "/def,starts_with,alphabet_pool"
    "/hijk,starts_with,alphabet_pool"
    "/lmnop,starts_with,alphabet_pool"
    "/bad_company,ends_with,api.co.com"
    "/superstition,contains,api.co.com"
    "/jimmyhendrix/purplehaze,equals,api.co.com"}


proc starts_with { prefix main_string } {
    return [string match $prefix $main_string]
}

proc ends_with { suffix main_string } {
    if {[string range $main_string [expr {[string length $main_string] - [string length $suffix]}] end] == $suffix} {
        return 1
    } else {
        return 0
    }
}

proc contains { prefix main_string } {
    return [string first $prefix $main_string]
}

proc equals { target main_string } {
    return [string equal $target $main_string]
}
    

proc express { req_uri uri operator runtime } {
    return  [$operator $req_uri $uri]
}

    
proc process_requests { request_uri} {
    global rules
    foreach rule $rules {
        #set request_uri /fi
        set fields [split $rule ,]
        lassign $fields uri operator runtime
        puts "Checking $request_uri in $uri"
        if { [info exists operator] == 1 } {
            if { [$operator $request_uri $uri] == 1 } {
                puts "matched $request_uri $operator $uri, sending to $runtime"
                break
            }
        }
    }
}

process_requests "/bad_company"

