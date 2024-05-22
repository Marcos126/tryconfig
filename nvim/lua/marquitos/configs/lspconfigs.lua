local M = {}

local map = vim.keymap.set

M.on_attach = function(client, bufnr)
    local function opts(desc)
        return { buffer = bufnr, desc = "LSP " .. desc }
    end

end

return M
