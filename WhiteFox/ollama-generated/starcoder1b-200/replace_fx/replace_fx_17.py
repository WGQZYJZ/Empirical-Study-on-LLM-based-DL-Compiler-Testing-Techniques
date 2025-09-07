
**Note**: The `lower_level` function must be used instead of the corresponding non-lower level `upper_level` functions (`nn.*ReLU*`, `nn.Tanh*`, etc.) in case it is an input to a lower layer (e.g. the `Linear` and `BatchNorm1d` layers). If no `lower_level` function exists, please use `upper_level`.

For each node that invokes `lower_level` and `upper_level`, this method replaces `lower_level` with its corresponding `upper_level`. If `fallback_random` configuration is set or if the device is a CPU, the nodes invoking these functions will not be replaced and thus will not trigger the `gm.graph.erase_node(node) line`.

