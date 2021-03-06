with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "ats";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    darwin.cf-private
    darwin.apple_sdk.frameworks.CoreServices
    openssl
    ncurses
    curl
    python37
    python37Packages.pip
  ];
  shellHook = ''
    python -m venv .env
    source .env/bin/activate
    export MYENV=nix_ats
  '';
}

