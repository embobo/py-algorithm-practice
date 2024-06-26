import pytest

from src.algorithms.huffman_coding import Node, decode_huff  # noqa F401


class TestDecodeHuff:
    @pytest.mark.parametrize(
        "input, expected",
        [
            ("1001011", "ABACA"),
            ("001000001010111001110111011110010111111001001000110", "Rumpelstiltskin"),
            (
                "0100001110101110011101001100001101011001001011111011011001100001101111010100111110011101010011111001010101010011011001100001101111010100111110011100100101111101111010100111110001100001101101000",  # noqa E501
                "howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?",
            ),
        ],
    )
    def test_decode_huff(self, input: str, expected: str):
        pass
        # todo have to write the encoder
        # these inputs all are passing on hackerrank
