
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Comment out below two lines to run this model on CPU device.
        v2 = torch.rand_like(x1, ...)
        t1 = torch.nn.functional.dropout(v2, ...)
#         v3 = torch.nn.functional.linear(...)
        return v2


# Initializing the model and configuring its parameters:
m = Model()
gm = gm.GraphMode(m)
gm.compile(input_tensor=(1, 2, 2), dtype=torch.float)
gm.dump_dot("model.dot") # Graphviz dot file output


# The function is used for converting between the generated model and a PyTorch model.
class ConvertModel():
    def __init__(self, gm):
        self.gm = gm

    def convert(self):
        gm_graph = self.gm.forward()

        def _replace_linear(node):
            gm_graph.replace_node(
                node,
                torch.nn.functional.linear(
                    gm_graph.get_input_tensor(0), gm_graph.get_output_tensor(0)
                )
            )
            gm_graph.erase_node(node)

        gm_graph.for_each_node(_replace_linear)
        gm_graph.dump_dot("converted-model.dot")


# Convert the generated model to a PyTorch model:
ConvertModel(gm).convert()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
