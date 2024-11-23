interface Record {
    [key: string]: any;
}

class LytDB {
    private data: Record;

    constructor() {
        this.data = {};
    }

    create(key: string, value: any): any {
        if (this.data[key]) {
            throw new Error('Record already exists.');
        }
        this.data[key] = value;
        return this.data[key];
    }

    read(key: string): any {
        if (!this.data[key]) {
            throw new Error('Record not found.');
        }
        return this.data[key];
    }

    update(key: string, value: any): any {
        if (!this.data[key]) {
            throw new Error('Record not found.');
        }
        this.data[key] = value;
        return this.data[key];
    }

    delete(key: string): any {
        if (!this.data[key]) {
            throw new Error('Record not found.');
        }
        const deletedValue = this.data[key];
        delete this.data[key];
        return deletedValue;
    }

    list(): Record {
        return this.data;
    }
}

export default LytDB;