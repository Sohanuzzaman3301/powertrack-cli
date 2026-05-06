# Maintainer: Sohanuzzaman3301 <sohanuzzaman3301@github.com>
pkgname=powertrack-cli
pkgver=1.0.4
pkgrel=1
pkgdesc="A vibrant rainbow battery and power monitor for Linux terminal"
arch=('any')
url="https://github.com/Sohanuzzaman3301/powertrack-cli"
license=('MIT')
depends=('python')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Sohanuzzaman3301/powertrack-cli/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('SKIP') # You should update this with the actual sha256sum

package() {
    cd "${pkgname}-${pkgver}"
    install -Dm755 powertrack.py "${pkgdir}/usr/bin/powertrack"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
