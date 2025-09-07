# 1. Generate model with pattern.
class Model(torch.nn.Module):
    def __init__(self, insize, outsize):
        super().__init__()
        self.linear = torch.nn.Linear(insize, outsize)

    def forward(self, x):
        t1 =  torch.nn.functional.dropout(x, p=0.5, inplace=False)
        t2 = torch.rand_like(t1, dtype=torch.float32).type_as(t1)
        t2 = t1 + t2
        return self.linear(t2)

model  = Model(4, 4)


# 2. Generate inputs to the model
input  = torch.randn(1000, 35).cuda()



# 3. Replace with lowmem_dropout
for node in gm.graph.nodes():
    if node.kind == 'prim::Dropout':
        replacements[node] = get_replacement_from_op(torch.nn.functional._C._nn.lowmem_dropout)

 # 4. Erase the original dropout function nodes
  for node in model.named_modules(prefix="")(input):
    if isinstance(node, torch.nn.Dropout2d) and node != replacements[node]:
      gm.graph.erase_node(node)
