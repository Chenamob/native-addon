{
  "targets": [
    {
      "target_name": "greet",
      "cflags!": [ "-fno-exceptions"
 ],
      "cflags_cc!": [ "-fno-exceptions" 
],

      "sources": [
        "./src/greeting.cpp",
        "./src/index.cpp"
      ],

      "conditions": [
        ["OS==\"linux\"", {
            'libraries': [
                       "-L../src/lib/",
              '-lhellooo',
            ],
"ldflags": [
    "-Wl,-rpath,'$$ORIGIN'"
],
"cflags_cc": [
          "-fexceptions",
          "-fPIC",
          "-Wno-unknown-pragmas"
        ]
                  }],
        ["OS==\"win\"", {
          "libraries": [
            "../libhello.so"
          ],
"include_dirs": [
"/usr/lib/libhellooo.so.0"
],
"libraries": [
"/usr/lib/libhellooo.so.0"
],
"include_dirs": [
"/usr/lib/libhellooo.so.0"
],
          "copies": [
            {
            "../libhello.so"
            "/usr/lib/libhello.so"


              "destination": "<(module_root_dir)/build/Release/",
              "files": [ "<(module_root_dir)/libhello.so" ]
            }
          ]
        }],
],

      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }
  ]
}