
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def replace_fx(m, name: str, node: torch._C.Node, new_name: str):  # New functions to be added.
        with torch._C.no_grad():
            return m[new_name](node)


# Initializing the model
m = Model()


