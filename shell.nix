with import <nixpkgs> {};
let
  my-python-packages = python-packages: [
    python-packages.pip
    # python-packages.numpy
    # python-packages.pytelegrambotapi
  ];
  my-python = python311.withPackages my-python-packages;
in
  pkgs.mkShell {
    buildInputs = [
      bashInteractive
      my-python
    ];
    shellHook = ''
      export PIP_PREFIX="$(pwd)/_build/pip_packages"
      export PYTHONPATH="$(pwd)/_build/pip_packages/lib/python3.11/site-packages:$PYTHONPATH" 
      unset SOURCE_DATE_EPOCH
    '';
  }

