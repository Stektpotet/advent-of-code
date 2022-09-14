const std = @import("std");
const print = std.debug.print;

pub fn readInput(allocator: std.mem.Allocator) ![]u8  {
    const size_limit = std.math.maxInt(u32);
    return try std.io.getStdIn().readToEndAlloc(allocator, size_limit);
}

pub fn sum(values: []u64) u64 {
    var s: u64 = 0;
    for (values) |n| s += n;
    return s;
}

pub fn slidingWindowIncrementCount(data: std.ArrayList(u64), window_size: u64) u64 {
    var increment_count: u64 = 0;
    var last = sum(data.items[0..window_size]);
    
    var i: u64 = 1;
    while (i <= data.items.len - window_size) : (i+=1) {
        var current: u64 = sum(data.items[i..i+window_size]);
        if (current > last)
            increment_count += 1;
        last = current;
    }
    return increment_count;
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    const data_raw = try readInput(allocator);
    var lines = std.mem.split(u8, std.mem.trimRight(u8, data_raw, "\r\n"), "\r\n");
    var data = std.ArrayList(u64).init(allocator);
    while (lines.next()) |line_raw| {
        const line = std.mem.trimRight(u8, line_raw, "\r\n");
        try data.append(try std.fmt.parseInt(u64, line, 10));
    }

    print("{d}\n{d}\n", .{slidingWindowIncrementCount(data, 1), slidingWindowIncrementCount(data, 3)});
}