
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, training=True) # Training the model is mandatory to generate this pattern
        v2 = torch.rand_like(v1)
        return v2


# Initializing the model and compiling it for GPU
m = Model()
gm.compile(m, device="cuda", jit=False)


# Checking for valid use cases:
test_cases = [
    # The following patterns are not supported by this method.
    # They generate an error because this pattern requires an inplace function that is currently not supported in our implementation.
    # (t1, t2): [m.linear(x) for x in [t1]] for the model m:
    #     v1 = torch.nn.functional.dropout(t1, p=0.5, training=True) 
    #     v2 = gm.graph.apply_inplace(v1)
    #     v3 = gm.graph.apply(gm.graph.apply_inplace(self.linear), v2)
]


for test_case in test_cases:
    input_tensors, output_tensors = test_case
    print(f"\n