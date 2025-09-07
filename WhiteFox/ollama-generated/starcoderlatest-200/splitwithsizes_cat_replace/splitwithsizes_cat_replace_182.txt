
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [1] + [i for i in range(len(v1.shape)-1)]
        concatenated_tensor = torch.cat([v1[j] for j in range(len(split_sizes))], dim=-1)
        return v6


# Optimizing the model with splitwithsizes_cat function and its different arguments
from torch._C import _get_op_registration
op_reg  = _get_op_registration()
model = m.eval()
op_name_split_tensor = "aten::split"
op_name_cat_tensor = "aten::cat"
is_valid_splitwithsizes_cat = op_reg._find_matching_op([op_name_split_tensor, op_name_cat_tensor], model)

if is_valid_splitwithsizes_cat:
    from torch.fx import Graph
    graph = Graph(m)

    # Remove split and concat operations that don't have any downstream uses in the optimized graph.
    graph.find_topologically_sorted_nodes()
    for node in reversed(graph):
        op = node.op
        if op._schema.name in [op_name_split_tensor, op_name_cat_tensor]:
            # If all tensors of the output of this split operation are used in a downstream concatenation, then remove the split operation.
            for use in node.outputs:
                if use not in graph.inputs():
                    if torch._C._jit_get_graph(use).has_user_op() == True:
                        break
                else:
                    if torch._C._jit_get_graph(use) != graph:
                        break
            else: # The tensors of the output are all used in a downstream concatenation, remove split operation.
                op_node = node.detach().copy()
                node.destroy()
                if op_node is not None:
                    for use in op_node.outputs():
                        graph._insert_edge(op_node, use)

    m.register_buffer("_split_tensor_sizes", torch.tensor([v1[j] for j in range(len(split_sizes))]))
    return True
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
