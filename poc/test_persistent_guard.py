"""Regression tests for persistent-guard circuit selection."""
import unittest
from network_sim import Network, Relay, select_paths_persistent_guard

class PersistentGuardTests(unittest.TestCase):
    def test_node_disjoint(self):
        relays = [Relay(i, asn=i, juris="A", inferred_asn=i) for i in range(15)]
        paths = select_paths_persistent_guard(Network(relays), 4, relays[0], hops=3, disjoint="node")
        self.assertIsNotNone(paths)
        self.assertEqual(paths[0][0].rid, 0)
        ids = [r.rid for path in paths for r in path]
        self.assertEqual(len(ids), len(set(ids)))

    def test_as_disjoint(self):
        relays = [Relay(i, asn=i, juris="A", inferred_asn=i) for i in range(15)]
        paths = select_paths_persistent_guard(Network(relays), 4, relays[0], hops=3, disjoint="as")
        self.assertIsNotNone(paths)
        asns = [r.inferred_asn for path in paths for r in path]
        self.assertEqual(len(asns), len(set(asns)))

    def test_insufficient_relays(self):
        relays = [Relay(i, asn=i, juris="A", inferred_asn=i) for i in range(5)]
        self.assertIsNone(select_paths_persistent_guard(Network(relays), 2, relays[0], hops=3, disjoint="node"))

if __name__ == "__main__":
    unittest.main()
