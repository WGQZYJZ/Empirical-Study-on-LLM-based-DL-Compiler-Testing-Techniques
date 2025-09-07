
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1, 0.5)  # Dropout is not replaced and thus will not trigger the gm.graph.erase_node(node) line
        return v2


# Initializing the model
m = Model()

