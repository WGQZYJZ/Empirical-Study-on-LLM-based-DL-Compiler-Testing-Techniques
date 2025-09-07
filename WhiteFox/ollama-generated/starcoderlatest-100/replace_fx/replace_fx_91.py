
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5)
        t2 = torch.rand_like(t1)
        return (t1 + t2).sum()


# Fallback options:
gm = graphsurgeon.GraphMatcher(torch.__version__, opset_map={torch.onnx._ExportTypes.ONNX}, fallback_random=False, pattern_to_operation_map={'*': '*'})
gm.find_matches(m)
# gm.graph.erase_node(x1)  # x1 node is not in this model example (as it's not in the original input to forward function).
torch._C._jit_pass_erase_dead_code()
gm.apply(m)


