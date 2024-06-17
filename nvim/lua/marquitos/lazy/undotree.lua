return {
    "mbbill/undotree",

    config = function() 
        vim.keymap.set("n", "<leader>u", vim.cmd.UndotreeToggle)
        vim.opt.undofile = true
        vim.opt.undodir = "/home/angel/.config/nvim/undotree/"
    end
}

