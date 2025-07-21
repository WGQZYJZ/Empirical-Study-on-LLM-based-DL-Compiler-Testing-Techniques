'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.AdamW\ntorch.optim.AdamW(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.01, amsgrad=False)\n'
import torch
x = torch.rand(3, requires_grad=True)
optimizer = torch.optim.AdamW([x], lr=0.1)
print('Default values:')
print('lr = ', optimizer.param_groups[0]['lr'])
print('betas = ', optimizer.param_groups[0]['betas'])
print('eps = ', optimizer.param_groups[0]['eps'])
print('weight_decay = ', optimizer.param_groups[0]['weight_decay'])
print('amsgrad = ', optimizer.param_groups[0]['amsgrad'])
optimizer.step()
print('Updated values:')
print('lr = ', optimizer.param_groups[0]['lr'])