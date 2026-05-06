class PowertrackCli < Formula
  desc "Vibrant rainbow battery and power monitor for Linux terminal"
  homepage "https://github.com/Sohanuzzaman3301/powertrack-cli"
  url "https://github.com/Sohanuzzaman3301/powertrack-cli/archive/refs/tags/v1.0.4.tar.gz"
  sha256 "REPLACE_WITH_ACTUAL_SHA256"
  license "MIT"

  depends_on "python@3.13"

  def install
    bin.install "powertrack.py" => "powertrack"
  end

  test do
    system "#{bin}/powertrack", "--help"
  end
end
