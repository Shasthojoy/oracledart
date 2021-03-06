solutions = [
  { "name"        : "sdk",
    "url"         : "https://github.com/dart-lang/sdk.git",
    "deps_file"   : "DEPS",
    "managed"     : True,
    "custom_deps" : {
    },
    "safesync_url": "",
  },
  { "name"        : "oracledart",
    "url"         : "https://github.com/aam/oracledart.git",
    "custom_deps" : {
    },
    "custom_hooks": [{
      "pattern": ".",
      "action": ["python",
                 "oracledart/tools/gyp_oracledart.py"],
    }],
    "safesync_url": "",
  },
]
