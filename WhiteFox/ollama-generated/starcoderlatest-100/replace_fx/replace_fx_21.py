
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # invoke `torch.nn.functional.dropout` on the input tensor
        v2 = torch.rand_like(x1, requires_grad=True)      # invoke `torch.rand_like` on the input tensor
        return v2


# Expected Graph IRs for above model
class Model:
  def forward(self, x1):
    t0_input = _tg.TensorType([False], dtype=None, device=None, requires_grad=False)  # type: ignore[assignment]

    with gm.graph.forward():
      t1 = torch.nn.functional.dropout(x1, p=0.5)

      v0 = gm.get_ir_tensor(t0_input, [t1])
    return gm._make_tuple([v0])

# Initializing the model
m = Model()


