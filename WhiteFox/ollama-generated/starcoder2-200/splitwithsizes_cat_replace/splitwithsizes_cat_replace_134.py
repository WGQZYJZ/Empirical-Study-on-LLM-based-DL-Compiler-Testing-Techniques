# Initializing the model 
m = torch.nn.SplitWithSizes([2], dim=0)
m(input1), {"input": input1}
