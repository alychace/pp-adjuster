{
  description = "Script to automatically adjust power profile and notify user.";

  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/*.tar.gz";

  outputs = {
    self,
    nixpkgs,
  }: let
    allSystems = [
      "x86_64-linux"
      "aarch64-linux"
    ];
    forAllSystems = fn:
      nixpkgs.lib.genAttrs allSystems
      (system: fn {pkgs = import nixpkgs {inherit system;};});
  in {
    formatter = forAllSystems ({pkgs}: pkgs.alejandra);

    packages = forAllSystems ({pkgs}: {
      default = pkgs.python311Packages.buildPythonPackage {
        pname = "pp-adjuster";
        version = "0.1.0";

        src = ./.;

        propagatedBuildInputs = [
          pkgs.libnotify
          pkgs.power-profiles-daemon
        ];

        installPhase = ''
          mkdir -p $out/bin
          mkdir -p $out/data
          cp ${./pp-adjuster.py} $out/bin/pp-adjuster
          chmod +x $out/bin/pp-adjuster
        '';

        meta = with pkgs.lib; {
          description = "Automatically adjust power profile and notify user.";
          license = licenses.gpl3;
          maintainers = with maintainers; [alyraffauf];
          mainProgram = "pp-adjuster";
        };
      };
    });
  };
}
