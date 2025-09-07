
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.125)
        v2 = torch.rand_like(v1, requires_grad=False)
        return v2


# Fallback random configuration of model
# This can be set to True or False, and is used in conjunction with the fallback
# implementation (in csrc/graph_matcher/fallback.h). By default this flag is set
# to True. 
g = gm.build_graph(m)
gm.optimize_for_inference(g, torch.device("cpu"))


# Generating an input tensor for the model that contains a dropout node
x1 = torch.randn(1, 2, 2).to(torch.float32)
