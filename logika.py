from dataclasses import dataclass

npd_kai_nevirsija_1926 = lambda atlyginimas: 625 - 0.42 * (atlyginimas - 840)
npd_kai_virsija_1926 = lambda atlyginimas: 400 - 0.18 * (atlyginimas - 642)


@dataclass(frozen=True)
class AtlyginimoDuomenys:
    npd: float
    gpm: float
    psd: float
    vsd: float
    atlyginimas_i_rankas: float


def vsd(p_atlyginimas):
    """
     VSD - 12.52%
    """
    return p_atlyginimas / 100 * 12.52


def psd(p_atlyginimas):
    """
     VSD - 6.98%
    """
    return p_atlyginimas / 100 * 6.98


def gpm(p_atlyginimas):
    """
     GPM - 20.00%
    :param p_atlyginimas: atlyginimas po npd
    """
    return p_atlyginimas / 100 * 20


def npd(atlyginimas_burto: float) -> float:
    """
    NPD pagal 2023-01-01 https://www.vmi.lt/evmi/npd-pnpd-taikymas-20-str.-1
    :param atlyginimas_burto: atlyginimas ant popieriaus
    :return: npd
    """
    npd = 625
    if atlyginimas_burto < 840:
        return npd
    elif 840 <= atlyginimas_burto <= 1926:
        npd = npd_kai_nevirsija_1926(atlyginimas_burto)
    elif atlyginimas_burto > 1926:
        npd = npd_kai_virsija_1926(atlyginimas_burto)
    return npd if npd > 0 else 0


def atlyginimo_skaiciuokle(atlyginimas) -> AtlyginimoDuomenys:
    """
    Pagrindinis atlyginimo apskaičiavimas
    :param atlyginimas:
    :return:
    """
    npd_ = npd(atlyginimas)
    gpm_ = gpm(atlyginimas - npd_)
    psd_ = psd(atlyginimas)
    vsd_ = vsd(atlyginimas)
    atlyginimas_i_rankas = atlyginimas - (gpm_ + psd_ + vsd_)

    data = AtlyginimoDuomenys(npd_, gpm_, psd_, vsd_, atlyginimas_i_rankas)
    print(f"{data}")
    return data
