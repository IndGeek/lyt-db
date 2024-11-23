import LytDB from './index';

const db = new LytDB();

try {
    console.log('Creating records...');
    db.create('user1', { name: 'John', age: 30 });
    db.create('user2', { name: 'Sam', age: 25 });
} catch (error) {
    console.error(error.message);
}

try {
    console.log('Reading records...');
    console.log(db.read('user1'));
} catch (error) {
    console.error(error.message);
}

try {
    console.log('Updating user1...');
    db.update('user1', { name: 'Alice', age: 31 });
} catch (error) {
    console.error(error.message);
}

console.log('Current records:', db.list());

try {
    console.log('Deleting user2...');
    db.delete('user2');
} catch (error) {
    console.error(error.message);
}

console.log('Final records:', db.list());